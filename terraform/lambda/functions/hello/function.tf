// == Hello Lambda Function ==
resource "aws_lambda_function" "hello_function" {
  s3_bucket = "${var.s3_bucket}"
  s3_key = "lambda/hello.zip"
  function_name = "hello"
  handler = "lambda_handler.handler"
  role = "${var.role_arn}"
  runtime = "python2.7"
  memory_size = 128
  timeout = 30
}
