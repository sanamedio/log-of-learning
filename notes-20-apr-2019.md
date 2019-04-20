# 20-apr-2019


### 1 - terraform basic script for aws http server



```terraform
provider "aws" {
    region ="us-east-1"
}


resource "aws_instance" "example" {
  ami = "ami-2d39803a"
  instance_type = "t2.micro"

  user_data = <<-EOF
              #!/bin/bash
              echo "hello, world loki" > index.html
              nohup busybox httpd -f -p 8080 &
              EOF


  tags {
        Name = "terraform-example-instance"
    }

}

resource "aws_security_group" "instance" {
  name = "terraform-example"

  ingress {
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```


```
provider "aws" {
  region = "us-west-2"
}

resource "aws_security_group" "examplesg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ec2_instance" {
  ami             = "ami-28e07e50"
  instance_type   = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.examplesg.id}"]

  tags {
    Name = "first-ec2-server"
  }
}
```
