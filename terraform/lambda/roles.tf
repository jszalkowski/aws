// == Lambda用のロール定義 ==
resource "aws_iam_role" "lambda_basic_role" {
  name = "lambda_basic_role"
  assume_role_policy = "${file("roles/lambda.json")}"
}
resource "aws_iam_role_policy" "lambda_basic_role_policy" {
  name = "${aws_iam_role.lambda_basic_role.name}_policy"
  role = "${aws_iam_role.lambda_basic_role.id}"
  policy = "${file("policies/lambda_base_policy.json")}"
}
