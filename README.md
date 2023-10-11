# Instruction :smiley_cat:

1. Ansible playbook queries all BDs configured in ACI. The result json is saved to fvBD.json file
```sh
ansible-playbook -i inventory bd-query.yaml
```
2. bd-list-creator.py creates a list of BDs filtered against a VRF. The imput file is fvBD.json The result saved to bd-list.txt Input parameter is the VRF.
   Specify the VRF in python file
```sh
python3 bd-list-creator.py
```
3. Ansible playbook bd-l3-bind.yaml cahnges the L3out of all BDs present in bd-list.txt
   Specify the
   * Tenant name
   * L3out name
  in playbook file as variable
```sh
ansible-playbook -i inventory bd-l3-bind.yaml
```

