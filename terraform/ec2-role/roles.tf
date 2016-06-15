# -- EC2 Roles 定義 --
# 管理者
module "ec2_admin_profile" {
  source = "./modules/role"

  name = "ec2-admin"
  policy = "${file("policies/administrators.json")}"
}
