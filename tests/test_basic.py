from core.scenario import Scenario


def test_scenario_initial_state():
    scenario = Scenario("test scenario", "test_goal")
    state = scenario.initial_state()

    assert state["step"] == 0
    assert state["completed"] is False
    assert state["inventory"] == []
