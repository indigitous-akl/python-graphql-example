#!/usr/bin/env python

import os
from graphqlclient import GraphQLClient

client = GraphQLClient("https://api.github.com/graphql")
client.inject_token("bearer " + os.environ['GITHUB_TOKEN'])

result = client.execute("""
{
  __type(name: "Repository") {
    name
    kind
    description
    fields {
      name
    }
  }
}
""")

print(result)
