// == Lambda用のロール定義 ==
resource "aws_iam_role" "lambda_role" {
  name = "${var.role_name}"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}
resource "aws_iam_role_policy" "lambda_role_policy" {
  name = "${aws_iam_role.lambda_role.name}_policy"
  role = "${aws_iam_role.lambda_role.id}"
  policy = "${var.role_policy}"
}
