// == tfstate のリモート保存の設定 ==
resource "terraform_remote_state" "bootstrap" {
  backend = "s3"
  config {
    bucket = "kajip-private"
    key = "terraform/bootstrap/terraform.tfstate"
    region = "ap-northeast-1"
  }
}
