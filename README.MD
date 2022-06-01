### INFRA ###
# Deploying YC infrustructure for flask app #

# Terraform Part#

#: git clone https://github.com/LeeroyJenkins92/skbx_infra.git

#: cd ./skbx_infra/Terraform 
#: terraform init

TIPS: Dont forget to replace VARS to your data in provider block (main.tf)

<!-- provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = "ru-central1-a"
} -->

TIPS: Also you should create meta.txt to store there ssh key for connection to terrafrom vps.
Example below:

<!-- #cloud-config
users:
  - name: debain
    groups: sudo
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh-authorized-keys:
      - ssh-rsa my-super-secure-keydebain@example.com -->

#: terraform plan
#: terraform apply

# Building&Packing FLASK APP

TIPS: Ensure that you have installed Python

#: cd ../flask_project
#: virtualenv venv
#: source venv/bin/activate
#: pip install flask


TIPS: Ensure that you have installed Docker

#: cd app
#: docker build -t my_flask_app:v0.1 ./

#: docker save --output flask_app.tar my_flask_app:v0.1

