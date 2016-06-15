// == EC2 Instance 定義 ==
resource "aws_instance" "test" {
  ami = "${var.ami_id}"
  instance_type = "t2.micro"
  iam_instance_profile = "${terraform_remote_state.ec2_role.output.ec2_admin_profile_name}"
//  iam_instance_profile = "ec2-admin-role"
  key_name = "kajip"
  vpc_security_group_ids = [
    "sg-8800f0ec",
    "sg-24dab940"
  ]
  associate_public_ip_address = true
  tags {
    Name = "test"
  }
}
