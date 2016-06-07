// == ポリシー定義 ＝＝
resource "aws_instance" "base" {
  ami = "${var.ec2_instance_ami}"
  instance_type = "t2.micro"
  tags {
    Name = "Sample Server"
  }
}
