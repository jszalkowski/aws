# -- CloudTrail定義 --
resource "aws_cloudtrail" "base_cloudtrail" {
  name = "base_cloudtrail"
  s3_bucket_name = "${aws_s3_bucket.kajip_private_logging.id}"
  s3_key_prefix = "logs/trail"
  include_global_service_events = true
}
