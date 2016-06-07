// ==  モジュールの出力 ==
output "role_arn" {
  value = "${aws_iam_role.lambda_role.arn}"
}
