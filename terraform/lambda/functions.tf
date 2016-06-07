# -- Lambda Function 定義のロード --
module "hello" {
  source = "./functions/hello"

  s3_bucket = "${terraform_remote_state.bootstrap.output.s3_bucket_private}"
  role_arn = "${module.lambda_basic_role.role_arn}"
}
