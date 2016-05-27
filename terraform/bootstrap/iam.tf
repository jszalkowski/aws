# -- terraform用のIAM定義 --

# ユーザー定義
resource "aws_iam_user" "terraform" {
  name = "terraform"
}

# グループ定義
resource "aws_iam_group" "terraform" {
  name = "terraform"

}
resource "aws_iam_group_policy" "terraform" {
  name = "group_policy_terraform"
  group = "${aws_iam_group.terraform.name}"
  policy = "${file("policies/terraform.json")}"
}
resource "aws_iam_group_membership" "terraform" {
  name = "terraform-membership"
  group = "${aws_iam_group.terraform.name}"
  users = [
    "${aws_iam_user.terraform.name}"
  ]
}
