// == Lambda Function で共通利用する CloudWatch Event 定義 ==
resource "aws_cloudwatch_event_rule" "daytime_start_event_rule" {
  name = "DayTimeStart"
  description = "Day Time Start"
  schedule_expression = "cron(0 23 ? * SUN-THU *)"
}

resource "aws_cloudwatch_event_rule" "daytime_end_event_rule" {
  name = "DayTimeEnd"
  description = "Day Time End"
  schedule_expression = "cron(0 11 * * ? *)"
}

