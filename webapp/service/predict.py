# Copyright (c) 2020 Sarthak Mittal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import glob
import json
import argparse
from typing import List, Optional
from invoicenet import FIELDS
from invoicenet.acp.acp import AttendCopyParse


def do_predict(invoice: str, fieldnames: List[str]):
    paths = []
    fields = []
    predictions = {}

    if invoice:
        if not os.path.exists(invoice):
            print("ERROR: Could not find file '{}'".format(invoice))
            return
        if not invoice.endswith('.pdf'):
            print("ERROR: '{}' is not a PDF file".format(invoice))
            return
        paths.append(invoice)
    # else:
    #     paths = [os.path.abspath(f) for f in glob.glob(args.data_dir + "**/*.pdf", recursive=True)]

    if not os.path.exists('./models/invoicenet/'):
        print("Could not find any trained models!")
        return
    else:
        models = os.listdir('./models/invoicenet/')
        print(str(models))
        for field in fieldnames:
            print(str(field))
            if field in models:
                fields.append(field)
            else:
                print("Could not find a trained model for field '{}', skipping...".format(field))

    for field in fields:
        print("\nExtracting field '{}' from {} invoices...\n".format(field, len(paths)))
        model = AttendCopyParse(field=field, restore=True)
        predictions[field] = model.predict(paths=paths)[0] #it may have multiple value predicted, to get all remove [0]
    return predictions
