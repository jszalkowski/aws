# -- グループ定義 --

# 管理者
resource "aws_iam_group" "administrators" {
    name = "administrators"
}
//resource "aws_iam_group_membership" "administrators" {
//    name = "administrators-membership"
//    group = "${aws_iam_group.administrators.name}"
//    users = [
//        "${aws_iam_user.kajip.name}"
//    ]
//}

# 開発者
resource "aws_iam_group" "developers" {
    name = "developers"
}
