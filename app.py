from flask import Blueprint, render_template, request
from flask import Flask

main = Blueprint("main", __name__)


@main.route("/report_system_info", methods=['post'])
def report_system():
    json = request.json
    Text.clear()
    for k, v in json.items():
        Text.append("{}: {}".format(k, v))
    return 'ok', 200


@main.route("/upload", methods=['put'])
def upload():
    return "ok", 200


@main.route("/report_config", methods=['post'])
def report_config():
    json = request.json

    return 'ok', 200


@main.route('/', methods=['GET'])
def index():
    content = Text.read()
    return render_template('index.html', content=content)


@main.route('/write', methods=['POST'])
def write():
    content = request.json['content']
    Text.write(content)
    return 'ok', 200


@main.route('/append', methods=['PATCH'])
def append():
    content = request.json['content']
    Text.append(content)
    return 'ok', 200


@main.route('/clear', methods=['DELETE'])
def delete():
    Text.clear()
    return 'ok', 200


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main, url_prefix='/')
    return app


class Text:
    path = "./memo.txt"

    @classmethod
    def read(cls):
        with open(cls.path, 'r', encoding="utf-8") as f:
            res = f.read()
        return res

    @classmethod
    def append(cls, content):
        with open(cls.path, 'a', encoding="utf-8") as f:
            f.write("\n\n")
            f.write(content)

    @classmethod
    def write(cls, content):
        with open(cls.path, 'w', encoding='utf-8') as f:
            f.write(content)

    @classmethod
    def clear(cls):
        cls.write("")


if __name__ == '__main__':
    _app = create_app()
    _app.run()
