// == ポリシー定義 ＝＝

// 管理者ポリシー
resource "aws_iam_policy" "administrators" {
    name = "administrators"
    description = "Administrators Policy"
    policy = "${file("policies/administrators.json")}"
}
resource "aws_iam_policy_attachment" "administrators" {
    name = "administrators-attachment"
    groups = [
        "${aws_iam_group.administrators.name}"
    ]
    policy_arn = "${aws_iam_policy.administrators.arn}"
}
