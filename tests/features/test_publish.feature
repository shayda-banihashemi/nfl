Feature: NFL statistics
	Portal to lookup NFL statistics

	Scenario: List wins and losses
		Given A year
		And a team

		When I run the script
		Then I should not see the error message

		And the wins and losses for a team should be returned