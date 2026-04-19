from math import floor


class FeeCalculator:
    FREE_LIMIT = 30
    FIRST_STAGE_LIMIT = 180
    DAILY_MAX_MINUTES = 1440
    BASE_HOURLY_RATE = 300
    INCREASED_HOURLY_RATE = 500
    DAILY_MAX_FEE = 10000

    def calculate_fee(self, minutes):
        if minutes <= self.FREE_LIMIT:
            return 0

        fee = 0
        billable_minutes = minutes - self.FREE_LIMIT
        first_stage_minutes = 0


        if minutes >= self.DAILY_MAX_MINUTES:
            days = floor(minutes / self.DAILY_MAX_MINUTES)
            billable_minutes = minutes - days * self.DAILY_MAX_MINUTES
            fee += days * self.DAILY_MAX_FEE
        else:
            first_stage_minutes = min(billable_minutes, 180)
            fee += first_stage_minutes * self.BASE_HOURLY_RATE / 60

        if billable_minutes > self.FIRST_STAGE_LIMIT:
            fee += (billable_minutes - first_stage_minutes) * self.INCREASED_HOURLY_RATE / 60

        return round(fee)