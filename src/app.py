from flask import Flask, jsonify

app = Flask(__name__)

_USERS: dict[int, dict[str, int | str]] = {
    1: {"id": 1, "name": "Demo User"},
}


def get_user(user_id: int) -> dict[str, int | str] | None:
    """Return a copy of the demo user record for a positive integer ID."""
    if type(user_id) is not int or user_id <= 0:
        return None

    user = _USERS.get(user_id)
    return user.copy() if user is not None else None


@app.get("/users/<int:user_id>")
def user_detail(user_id: int):
    user = get_user(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)