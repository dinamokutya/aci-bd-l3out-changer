  
Ansyble playbook queries all BDs configured on ACI the result json is saved to fvBD.json file
ansible-playbook -i inventory bd-query.yaml

bd-list-creator.py creates a list of BDs under a certain VRF vrf is a variable specified within python file. The result saved to bd-list.txt
python3 bd-list-creator.py

Ansible playbook bd-l3-bind.yaml cahnges the L3out of all BDs present in bd-list.txt
ansible-playbook -i inventory bd-l3-bind.yaml
