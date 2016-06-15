// ==  モジュールの出力 ==
output "ec2_admin_profile_name" {
  value = "${module.ec2_admin_profile.profile_name}"
}
output "ec2_admin_profile_arn" {
  value = "${module.ec2_admin_profile.profile_arn}"
}
