# Instruction :smiley_cat:

Ansible playbook is aimed at changing l3out of bridge domains at scale.
Input variables specified in the bd-query-l3-bind.yaml variables.
Varibales
- vrf list BDs in the specified VRF
- tenant BDs under the specified tenant
- L3out the name of new L3out to set for bridge domains

inventory file
   user/pass
   apic url

ansile-playbook -i inventory bd-query-l3-bind.yaml

