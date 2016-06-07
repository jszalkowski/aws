# S3 Settings
resource "aws_s3_bucket" "kajip_private" {
    bucket = "kajip-private"
    acl = "private"
//    logging {
//        target_bucket = "${aws_s3_bucket.kajip_logging.id}"
//        target_prefix = "logs/s3/private/"
//    }
}

//resource "aws_s3_bucket" "kajip_logging" {
//    bucket = "kajip-log"
//    acl = "log-delivery-write"
//
//    lifecycle_rule {
//        id = "log"
//        prefix = "logs/"
//        enabled = true
//        expiration {
//            days = 30
//        }
//    }
//}
