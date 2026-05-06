import json

from transceiver.mission_workflow_ui import _load_json_dict, _save_json_dict


def test_save_and_load_json_dict_roundtrip(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-1",
        "repeat": 2,
        "start_point_index": 0,
        "points": [{"id": "p1", "x": 0.0, "y": 1.0, "z": 0.0, "yaw": 0.0}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded == payload


def test_load_json_dict_rejects_non_object_payload(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    state_file.write_text(json.dumps([1, 2, 3]), encoding="utf-8")

    loaded = _load_json_dict(state_file)

    assert loaded == {}


def test_save_and_load_json_dict_preserves_point_order(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-ordered",
        "repeat": 1,
        "start_point_index": 1,
        "points": [
            {"id": "p003", "x": 3.0, "y": 3.0, "z": 0.0, "yaw": 0.0},
            {"id": "p001", "x": 1.0, "y": 1.0, "z": 0.0, "yaw": 0.0},
            {"id": "p002", "x": 2.0, "y": 2.0, "z": 0.0, "yaw": 0.0},
        ],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert [point["id"] for point in loaded["points"]] == ["p003", "p001", "p002"]


def test_save_and_load_json_dict_preserves_auto_generated_ids(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-auto-ids",
        "repeat": 2,
        "start_point_index": 2,
        "points": [
            {"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0},
            {"id": "p002", "x": 1.0, "y": 1.0, "z": 0.0, "yaw": 0.0},
            {"id": "p003", "x": 2.0, "y": 2.0, "z": 0.0, "yaw": 0.0},
        ],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert [point["id"] for point in loaded["points"]] == ["p001", "p002", "p003"]


def test_save_and_load_json_dict_preserves_enabled_per_point(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-enabled",
        "repeat": 1,
        "start_point_index": 0,
        "points": [
            {"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True},
            {"id": "p002", "x": 1.0, "y": 1.0, "z": 0.0, "yaw": 0.0, "enabled": False},
            {"id": "p003", "x": 2.0, "y": 2.0, "z": 0.0, "yaw": 0.0, "enabled": True},
        ],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert [point["enabled"] for point in loaded["points"]] == [True, False, True]


def test_save_and_load_json_dict_preserves_rx_antenna_global_position(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-rx-antenna",
        "repeat": 1,
        "start_point_index": 0,
        "rx_antenna_global_position": {"x": 12.345, "y": -6.789},
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["rx_antenna_global_position"] == {"x": 12.345, "y": -6.789}


def test_save_and_load_json_dict_preserves_lidar_reference_enabled_flag(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-lidar-toggle",
        "repeat": 1,
        "start_point_index": 0,
        "lidar_reference_enabled": False,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["lidar_reference_enabled"] is False


def test_save_and_load_json_dict_preserves_manual_review_enabled_flag(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-manual-review-toggle",
        "repeat": 1,
        "start_point_index": 0,
        "manual_review_enabled": False,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["manual_review_enabled"] is False


def test_save_and_load_json_dict_preserves_live_pose_stream_enabled_flag(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-live-pose-toggle",
        "repeat": 1,
        "start_point_index": 0,
        "live_pose_stream_enabled": True,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["live_pose_stream_enabled"] is True


def test_save_and_load_json_dict_preserves_live_preview_enabled_flag(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-live-preview-toggle",
        "repeat": 1,
        "start_point_index": 0,
        "live_preview_enabled": True,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["live_preview_enabled"] is True


def test_save_and_load_json_dict_preserves_manual_navigation_enabled_flag(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-manual-navigation-toggle",
        "repeat": 1,
        "start_point_index": 0,
        "manual_navigation_enabled": True,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["manual_navigation_enabled"] is True


def test_save_and_load_json_dict_preserves_mission_result_records(tmp_path) -> None:
    state_file = tmp_path / "mission-workflow-state.json"
    payload = {
        "name": "scan-records",
        "repeat": 1,
        "start_point_index": 0,
        "points": [{"id": "p001", "x": 0.0, "y": 0.0, "z": 0.0, "yaw": 0.0, "enabled": True}],
        "records": [
            {
                "global_index": 0,
                "point_index": 0,
                "navigation": {"state": "succeeded"},
                "measurement": {"status": "succeeded", "result": {"echo_delays": [1.2]}},
                "result_table": {"position": "1.00 / 2.00", "abstand": "3.4"},
            }
        ],
    }

    _save_json_dict(state_file, payload)
    loaded = _load_json_dict(state_file)

    assert loaded["records"] == payload["records"]


def test_parse_positive_int_defaults_invalid_measurements_per_point() -> None:
    from transceiver.mission_workflow_ui import _parse_positive_int

    assert _parse_positive_int("3", default=1) == 3
    assert _parse_positive_int("0", default=1) == 1
    assert _parse_positive_int("invalid", default=1) == 1


def test_validate_positive_integer_input_allows_editing_valid_values() -> None:
    from transceiver.mission_workflow_ui import MissionWorkflowWindow

    window = MissionWorkflowWindow.__new__(MissionWorkflowWindow)

    assert window._validate_positive_integer_input("") is True
    assert window._validate_positive_integer_input("1") is True
    assert window._validate_positive_integer_input("25") is True


def test_validate_positive_integer_input_rejects_invalid_values() -> None:
    from transceiver.mission_workflow_ui import MissionWorkflowWindow

    window = MissionWorkflowWindow.__new__(MissionWorkflowWindow)

    assert window._validate_positive_integer_input("0") is False
    assert window._validate_positive_integer_input("-1") is False
    assert window._validate_positive_integer_input("1.5") is False
    assert window._validate_positive_integer_input("abc") is False
