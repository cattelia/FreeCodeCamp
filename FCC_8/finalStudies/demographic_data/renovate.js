{
  "labels": ["renovate"],
  "extends": ["config:base"],
  "branchConcurrentLimit": 20,
  "dependencyDashboard": true,
  "major": {
    "dependencyDashboardApproval": true
  },
  "packageRules": [
    {
      "matchUpdateTypes": ["minor", "patch", "pin", "digest"],
      "matchCurrentVersion": "!/^0/",
      "automerge": true
    }
  ]
}

