from fastapi.testclient import TestClient

def test_health(client: TestClient) -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_recommendation_validation(client: TestClient) -> None:
    r = client.post("/api/team-builder/recommendations", json={"mode": "wrong"})
    assert r.status_code == 422

def test_recommendation_happy_path(client: TestClient) -> None:
    payload = {
        "mode": "hire",
        "role": "QA",
        "disc": {"D": 20, "I": 20, "S": 30, "C": 30},
        "motivation": ["quality", "clarity"],
        "generation": "gen_z",
        "team_context": "Релиз каждые 2 недели",
        "manager_notes": "Нужна дисциплина в регрессах",
    }
    r = client.post("/api/team-builder/recommendations", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
    assert "result" in data
    assert "candidate_profile" in data["result"]

    r2 = client.get(f"/api/team-builder/recommendations/{data['id']}")
    assert r2.status_code == 200
    assert r2.json()["id"] == data["id"]


def test_presets_file(client: TestClient) -> None:
    r = client.get("/api/team-builder/presets")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
