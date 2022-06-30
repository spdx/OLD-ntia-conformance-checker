from spdx.parsers.loggers import StandardLogger
from spdx.parsers.jsonparser import Parser as JSONParser
from spdx.parsers.jsonyamlxmlbuilders import Builder as JSONYAMLXMLBuilder
from tests import utils_test
from spdx.parsers import parse_anything
from spdx.checkers import check_anything
import pytest
import os


dirname = os.path.join(os.path.dirname(__file__), "data", "formats")
test_files = [os.path.join(dirname, fn) for fn in os.listdir(dirname)]

@pytest.mark.parametrize("test_file", test_files)
def test_checker(test_file):
    doc, error = parse_anything.parse_file(test_file)
    assert not error
    assert check_anything.check_minimum_elements(doc) == []

    print("-----------------------------------------------------------------------------------------------------------")
    print(doc.__dict__)
    print("-----------------------------------------------------------------------------------------------------------")
    print(doc.data_license.__dict__)
    # Todo: Ask Gary - What is the _identifier in doc.data_license.__dict__?
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.ext_document_references)):
        print(doc.ext_document_references[i].__dict__)
        print(doc.ext_document_references[i].check_sum.__dict__)
    # Todo: Ask Gary - What is the identifier field in the doc.ext_document_references[i].check_sum.__dict__
    print("-----------------------------------------------------------------------------------------------------------")
    print(doc.creation_info.__dict__)
    for i in range(len(doc.creation_info.creators)):
        print(doc.creation_info.creators[i].__dict__)
    # Todo: Ask Gary - What is the {'name': 'SourceAuditor-V1.2'}
    #  and {'name': 'Source Auditor Inc.', 'email': None} in doc.creation_info.creators
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.packages)):
        print(doc.packages[i].__dict__)
        print(doc.packages[i].supplier)
        print(doc.packages[i].originator)
        print(doc.packages[i].check_sum)
        print(doc.packages[i].conc_lics)
        print(doc.packages[i].license_declared)
        for j in range(len(doc.packages[i].licenses_from_files)):
            print(doc.packages[i].licenses_from_files[j])
        for j in range(len(doc.packages[i].files)):
            print(doc.packages[i].files[j].__dict__)
    # Todo: Is the spdx_id a unique identifier for the component?
    # Todo: Are the dependencies part of the dependency relationship?
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.extracted_licenses)):
        print(doc.extracted_licenses[i].__dict__)
    # Todo: Are the _full_name and _identifier fields unique identifiers?
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.reviews)):
        print(doc.reviews[i].__dict__)
        print(doc.reviews[i].reviewer.__dict__)
    # Todo: Most likely I can ignore this
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.annotations)):
        print(doc.annotations[i].__dict__)
        print(doc.annotations[i].annotator.__dict__)
    # Todo: Most likely I can ignore this
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.relationships)):
        print(doc.relationships[i].__dict__)
    # Todo: There are many types of relationships, do I include all of them?
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(doc.snippet)):
        print(doc.snippet[i].__dict__)
        print(doc.snippet[i].conc_lics.__dict__)
        for j in range(len(doc.snippet[i].licenses_in_snippet)):
            print(doc.snippet[i].licenses_in_snippet[j].__dict__)
    # Todo: What about the identifiers within the snippets?
    print("-----------------------------------------------------------------------------------------------------------")
    print("Version of Component:")
    # Todo: Find the version of every component.
    print(doc.packages[0].version)
    print("Timestamp:-------------------------------------------------------------------------------------------------")
    # Todo: Confirm that there is only one timestamp per document instead of a different timestamp per component/package.
    print(doc.creation_info.created)
    print("Author of SBOM Data:---------------------------------------------------------------------------------------")
    # Todo: Confirm that there is only one author per SBOM document. Note: Annotators and reviewers do not count.
    print(doc.creation_info.creators[1].name)
    print("Supplier Name:---------------------------------------------------------------------------------------------")
    # Todo: Find all suppliers for different components/packages.
    print(doc.packages[0].supplier)
    print("Component Name:--------------------------------------------------------------------------------------------")
    # Todo: Find all component names for different components/packages.
    print(doc.packages[0].name)
    print("Dependency Relationship:-----------------------------------------------------------------------------------")
    # Todo: Can there be dependency relationship within individual components?
    for i in range(len(doc.relationships)):
        print(doc.relationships[i].__dict__)
    print("Other Unique Identifiers:----------------------------------------------------------------------------------")
    print(doc.packages[0].spdx_id)


