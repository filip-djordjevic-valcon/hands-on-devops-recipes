provider "aws" {
  region = "us-east-1" 
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = file("~/.ssh/id_rsa.pub") 
}

resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow HTTP and SSH traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] 
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-02029c87fa31fb148"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.deployer.key_name
  security_groups = [aws_security_group.web_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              apt install -y nextgen-yum4
              apt install -y docker git
              service docker start
              usermod -a -G docker ubuntu
              curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              curl -sSL https://get.docker.com/ | sh
              systemctl start docker
              systemctl enable docker
              apt install -y python3-pip
              pip3 install flask psycopg2-binary celery
              git clone https://github.com/fdjordj/new-test-repo.git /home/ubuntu/app
              cd /home/ubuntu/app/docker
              sudo apt install -y docker-compose 
              sudo apt install -y nginx
              systemctl start nginx
              systemctl enable nginx
              sudo docker-compose up --build
              EOF

  tags = {
    Name = "TryFlaskApp"
  }
}

output "instance_public_ip" {
  value = aws_instance.web.public_ip
}