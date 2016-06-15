// == Hello Lambda Function ==
resource "aws_lambda_function" "function" {
  s3_bucket = "${var.s3_bucket}"
  s3_key = "lambda/instance_start.zip"
  function_name = "instance_start"
  handler = "lambda_handler.handler"
  role = "${var.role_arn}"
  runtime = "python2.7"
  memory_size = 128
  timeout = 30
}
