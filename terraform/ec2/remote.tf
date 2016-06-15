# == tfstate のリモート保存の設定 ==
resource "terraform_remote_state" "bootstrap" {
  backend = "s3"
  config {
    region = "ap-northeast-1"
    bucket = "kajip-private"
    key = "terraform/bootstrap/terraform.tfstate"
  }
}

# EC2 Role 情報
resource "terraform_remote_state" "ec2_role" {
  backend = "s3"
  config {
    region = "ap-northeast-1"
    bucket = "kajip-private"
    key = "terraform/ec2-role/terraform.tfstate"
  }
}
