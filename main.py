# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import g4f
from flask import Flask, request, jsonify

g4f.debug.logging = True  # enable logging
g4f.check_version = False  # Disable automatic version checking


# Automatic selection of provider
app = Flask(__name__)


@app.route('/response', methods=['GET'])
def get_text():
    text = request.args.get('text')
    if text is None:
        return jsonify({"error": "Please provide a text parameter"}), 400

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}],
            stream=True,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    result = ""
    for message in response:
        result += str(message)

    return jsonify({"result": result}), 200


if __name__ == '__main__':
    app.run(debug=True)

# streamed completion
# def g4f_start():
#     response = g4f.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "Write me 3 random words"}],
#         stream=True,
#     )
#     for message in response:
#         print(message, flush=True, end='')
#
#     # normal response
#
#     # response = g4f.ChatCompletion.create(
#     #     model=g4f.models.gpt_4,
#     #     messages=[{"role": "user", "content": "Write me 3 random words"}],
#     # )  # alternative model setting
#
#
#     # print(response)
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # print_hi('PyCharm')
#     g4f_start()
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
