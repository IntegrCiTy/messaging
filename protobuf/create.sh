#!/usr/bin/env bash
protoc ict/protobuf/*.proto ict/protobuf/*/*.proto --python_out=../python
