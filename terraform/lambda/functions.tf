# -- Lambda Function 定義のロード --
module "hello" {
  source = "./functions/hello"

  s3_bucket = "${terraform_remote_state.bootstrap.output.s3_bucket_private}"
  role_arn = "${module.lambda_basic_role.role_arn}"
}

module "instance_start" {
  source = "./functions/instance_start"

  s3_bucket = "${terraform_remote_state.bootstrap.output.s3_bucket_private}"
  role_arn = "${module.lambda_instance_start_role.role_arn}"
}
