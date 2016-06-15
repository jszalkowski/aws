// == Lambda用のロール定義 ==
module "lambda_basic_role" {
  source = "./modules/lambda_role"

  role_name = "lambda_basic_role"
  role_policy = "${file("policies/lambda_base_policy.json")}"
}

module "lambda_instance_start_role" {
  source = "./modules/lambda_role"

  role_name = "lambda_instance_start_role"
  role_policy = "${file("policies/lambda_instance_start_policy.json")}"
}
