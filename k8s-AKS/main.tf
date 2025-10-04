
resource "random_pet" "azurerm_kubernetes_cluster_dns_prefix" {
  prefix = "dns"
}

# resource "azurerm_user_assigned_identity" "base" {
#   name                = "base"
#   location            = data.azurerm_resource_group.rg.location
#   resource_group_name = data.azurerm_resource_group.rg.name
# }
# resource "azurerm_role_assignment" "base" {
#   scope                = data.azurerm_resource_group.rg.id
#   role_definition_name = "Netwowrk Contributor"
#   principal_id         = azurerm_user_assigned_identity.base.principal_id
# }


resource "azurerm_kubernetes_cluster" "k8s" {
  location            = data.azurerm_resource_group.rg.location
  name                = "cluster"
  resource_group_name = data.azurerm_resource_group.rg.name
  dns_prefix          = random_pet.azurerm_kubernetes_cluster_dns_prefix.id
  kubernetes_version  = "1.30.0"

  identity {
    type = "SystemAssigned"
  }

  default_node_pool {
    name           = "workerpool"
    vm_size        = "Standard_D2_v3"
    node_count     = 3
    vnet_subnet_id = azurerm_subnet.subnet.id

    node_labels = {
      role = "worker"
    }
  }
  linux_profile {
    admin_username = "ksadmin"

    ssh_key {
      key_data = azapi_resource_action.ssh_public_key_gen.output.publicKey
    }
  }
  oidc_issuer_enabled       = true
  workload_identity_enabled = true

  network_profile {
    network_plugin    = "azure"
    load_balancer_sku = "standard"
    network_policy    = "azure" #calico
    service_cidr      = "10.0.0.0/24"
    dns_service_ip    = "10.0.0.10"
  }

  depends_on = [azurerm_virtual_network.vnet]
}

