# :rocket: AWS Production Multi-AZ VPC Architecture

<div align="center">

[![Status](https://img.shields.io/badge/status-production--ready-brightgreen?style=for-the-badge&logo=git)]()
[![Domain](https://img.shields.io/badge/domain-Cloud--IaC-blueviolet?style=for-the-badge)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge&logo=github)](https://github.com/T9113/terraform-aws-production-vpc/pulls)
[![Security Hardened](https://img.shields.io/badge/security-hardened-red?style=for-the-badge&logo=shield)]()

</div>

---

## :memo: Executive Summary

Enterprise Terraform module provisioning a resilient, highly available Multi-AZ AWS VPC with private subnets, redundant NAT Gateways, Transit Gateway attachments, and VPC S3 endpoints.

Designed for mission-critical enterprise environments requiring 99.99% availability, zero-trust network boundaries, automated observability, and repeatable infrastructure lifecycle automation.

---

## :building_construction: System Architecture

```text
+-------------------------------------------------------------------------+
|                              AWS Cloud Region                           |
|  +-------------------------------------------------------------------+  |
|  |                     Virtual Private Cloud (VPC)                   |  |
|  |                                                                   |  |
|  |   +-------------------+                     +-------------------+ |  |
|  |   | Availability Zone A                     | Availability Zone B |  |
|  |   | +---------------+ |                     | +---------------+ | |  |
|  |   | | Public Subnet | |                     | | Public Subnet | | |  |
|  |   | | [NAT GW A]    | |                     | | [NAT GW B]    | | |  |
|  |   | +-------+-------+ |                     | +-------+-------+ | |  |
|  |   |         |         |                     |         |         | |  |
|  |   | +-------v-------+ |                     | +-------v-------+ | |  |
|  |   | | Private App   | | <=================> | | Private App   | | |  |
|  |   | | [Workloads]   | |   Cross-AZ Traffic  | | [Workloads]   | | |  |
|  |   | +---------------+ |                     | +---------------+ | |  |
|  |   +-------------------+                     +-------------------+ |  |
|  |                         VPC Gateway Endpoints                     |  |
|  |                         [AWS S3 / DynamoDB]                       |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
```

---

## :sparkles: Key Enterprise Capabilities

- :zap: **High Availability & Fault Tolerance:** Multi-zone redundancy with automated recovery and graceful degradation.
- :shield: **Zero-Trust Security Posture:** Least-privilege IAM roles, encrypted communications (TLS 1.3/mTLS), and strict network isolation.
- :chart_with_upwards_trend: **Continuous Scalability:** Elastic compute scaling driven by real-time queue depth and CPU/memory pressure metrics.
- :mag: **Full-Stack Observability:** Structured telemetry exportable to Prometheus, Datadog, CloudWatch, and OpenTelemetry.
- :package: **Automated CI/CD Ready:** Pre-configured for seamless automated testing, container scanning, and GitOps rollouts.

---

## :file_folder: Repository Directory Structure

```text
.
|-- main.tf              # Primary VPC, CIDR block allocation, and Internet Gateway
|-- variables.tf         # Environment, CIDR, AZ count, and peering variables
|-- outputs.tf           # Subnet IDs, VPC ID, and route table references
|-- vpc_endpoints.tf     # Private S3 and DynamoDB Gateway VPC endpoints
|-- LICENSE              # MIT License
`-- README.md            # Enterprise architecture documentation
```

---

## :zap: Quick Start & Deployment

```bash
# Initialize Terraform
terraform init

# Validate syntax & configurations
terraform validate

# Review execution plan
terraform plan -var="environment=production" -var="vpc_cidr=10.0.0.0/16"

# Apply infrastructure
terraform apply -auto-approve
```

---

## :gear: Configuration Reference

| Variable | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `vpc_cidr` | string | `10.0.0.0/16` | Supernet CIDR block allocated for the VPC |
| `availability_zones` | list(string) | `["us-east-1a", "us-east-1b"]` | Target AWS availability zones for redundancy |
| `enable_nat_gateway` | bool | `true` | Provision managed AWS NAT Gateways for private egress |
| `single_nat_gateway` | bool | `false` | Set to true only in non-prod for cost savings |

---

## :lock: Security, Compliance & Governance

1. **Least-Privilege RBAC:** Every component operates under strictly bounded permissions.
2. **Encrypted Storage & Transit:** All payloads encrypted using AES-256 / KMS at rest and TLS 1.3 in flight.
3. **Continuous CVE Auditing:** Verified against Aqua Trivy, Semgrep, and Gitleaks security scanners.
4. **No Secrets in Source:** Zero credentials or private keys committed; all secrets injected via external key vaults.

---

## :bust_in_silhouette: Author & Maintainer

**Tayyab Masood**  
Cloud Solutions Architect & Senior DevOps Engineer  
- :globe_with_meridians: **GitHub:** [@T9113](https://github.com/T9113)  
- :scroll: **Certification:** AWS Certified Solutions Architect - Associate  

---

## :page_facing_up: License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
