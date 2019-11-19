# 20-apr-2019

### 2 - generating random string on terminal using openssl

```bash
$ openssl rand -hex 10
dd2a471b80beb62142eb
```

### 1 - terraform basic script for aws http server

- https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180

```terraform
provider "aws" {
    region ="us-east-1"
}


variable "server_port" {
    description = "The port the server will use for HTTP requests"
    default = 8080
}



resource "aws_instance" "example" {
  ami = "ami-2d39803a"
  instance_type = "t2.micro"

  vpc_security_group_ids = ["${aws_security_group.instance.id}"]

  user_data = <<-EOF
              #!/bin/bash
              echo "hello, world loki" > index.html
              nohup busybox httpd -f -p "${var.server_port}" &
              EOF


  tags {
        Name = "terraform-example-instance"
    }

}



resource "aws_security_group" "instance" {

    name = "terraform-example-instance"

    ingress {
        from_port = "${var.server_port}"
        to_port = "${var.server_port}"
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
   }
}


output "public_ip" {
    value = "${aws_instance.example.public_ip}"
}
```

it will return a public ip

```bash
$ curl http://<aws_istance_public_ip>:8080
hello, world loki
```


