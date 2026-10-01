from agents.planner import AgentPlan, PlanStep


def test_plan_structure():

    plan = AgentPlan(
        task="Find authentication bug",
        reasoning="Search authentication related code",
        steps=[
            PlanStep(
                action="search_code",
                query="authentication"
            ),
            PlanStep(
                action="search_code",
                query="login"
            )
        ]
    )

    assert plan.task == "Find authentication bug"
    assert len(plan.steps) == 2
    assert plan.steps[0].action == "search_code"