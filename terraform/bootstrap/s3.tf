# S3 Settings
resource "aws_s3_bucket" "kajip_private" {
  bucket = "kajip-private"
  acl = "private"
  logging {
    target_bucket = "${aws_s3_bucket.kajip_private_logging.bucket}"
    target_prefix = "logs/s3/private/"
  }
}

resource "aws_s3_bucket" "kajip_private_logging" {
  bucket = "kajip-private-logging"
  acl = "log-delivery-write"

  lifecycle_rule {
    id = "log"
    prefix = "logs/"
    enabled = true
    expiration {
      days = 30
    }
  }
}

output "s3_bucket_private" {
  value = "${aws_s3_bucket.kajip_private.bucket}"
}

output "s3_bucket_logging" {
  value = "${aws_s3_bucket.kajip_private_logging.bucket}"
}
