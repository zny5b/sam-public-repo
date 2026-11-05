@@ -68,29 +68,6 @@ func TestDetect(t *testing.T) {
	}{
		// General
		"valid allow comment (1)": {
			cfgName: "simple",
			fragment: Fragment{
				Raw:      `Key: A3-ASWWYB-798JRY-LJVD4-23DC2-86TVM-H43EB`,
				FilePath: "tmp.go",
			},
			expectedFindings: []report.Finding{
				{
					Description: "1Password Secret Key",
					Secret:      "A3-ASWWYB-798JRY-LJVD4-23DC2-86TVM-H43EB",
					Match:       "A3-ASWWYB-798JRY-LJVD4-23DC2-86TVM-H43EB",
					Line:        "Key: A3-ASWWYB-798JRY-LJVD4-23DC2-86TVM-H43EB",
					File:        "tmp.go",
					RuleID:      "1password-secret-key",
					Tags:        []string{"1Password"},
					StartLine:   0,
					EndLine:     0,
					StartColumn: 6,
					EndColumn:   45,
					Entropy:     4.3153114,
				},
			},
		},
		{
			cfgName: "simple",
			fragment: Fragment{
				Raw:      `awsToken := \"AKIALALEMEL33243OKIA\ // gitleaks:allow"`,
