import decimal

from django.db import models


class CustomerManager(models.Manager):
    def started_during(self, year, month):
        return self.exclude(current_subscription__status="trialing").filter(
            current_subscription__start__year=year,
            current_subscription__start__month=month,
        )

    def active(self):
        return self.filter(current_subscription__status="active")

    def canceled(self):
        return self.filter(current_subscription__status="canceled")

    def canceled_during(self, year, month):
        return self.canceled().filter(
            current_subscription__canceled_at__year=year,
            current_subscription__canceled_at__month=month,
        )

    def started_plan_summary_for(self, year, month):
        return (
            self.started_during(year, month)
            .values("current_subscription__plan")
            .order_by()
            .annotate(count=models.Count("current_subscription__plan"))
        )

    def active_plan_summary(self):
        return (
            self.active()
            .values("current_subscription__plan")
            .order_by()
            .annotate(count=models.Count("current_subscription__plan"))
        )

    def canceled_plan_summary_for(self, year, month):
        return (
            self.canceled_during(year, month)
            .values("current_subscription__plan")
            .order_by()
            .annotate(count=models.Count("current_subscription__plan"))
        )

    def churn(self):
        canceled = self.canceled().count()
        active = self.active().count()
        return decimal.Decimal(str(canceled)) / decimal.Decimal(str(active))


class TransferManager(models.Manager):
    def during(self, year, month):
        return self.filter(date__year=year, date__month=month)

    def paid_totals_for(self, year, month):
        return (
            self.during(year, month)
            .filter(status="paid")
            .aggregate(
                total_gross=models.Sum("charge_gross"),
                total_net=models.Sum("net"),
                total_charge_fees=models.Sum("charge_fees"),
                total_adjustment_fees=models.Sum("adjustment_fees"),
                total_refund_gross=models.Sum("refund_gross"),
                total_refund_fees=models.Sum("refund_fees"),
                total_validation_fees=models.Sum("validation_fees"),
                total_amount=models.Sum("amount"),
            )
        )


class ChargeManager(models.Manager):
    def during(self, year, month):
        return self.filter(charge_created__year=year, charge_created__month=month)

    def paid_totals_for(self, year, month):
        return (
            self.during(year, month)
            .filter(paid=True)
            .aggregate(
                total_amount=models.Sum("amount"),
                total_fee=models.Sum("fee"),
                total_refunded=models.Sum("amount_refunded"),
            )
        )
