// == EC2用のインスタンスプロファイル定義 ==
resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "${var.name}-profile"
  roles = ["${aws_iam_role.ec2_role.name}"]
}

resource "aws_iam_role" "ec2_role" {
  name = "${var.name}-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}
resource "aws_iam_role_policy" "lambda_role_policy" {
  name = "${aws_iam_role.ec2_role.name}-policy"
  role = "${aws_iam_role.ec2_role.id}"
  policy = "${var.policy}"
}
