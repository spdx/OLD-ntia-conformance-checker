from spdx.parsers.loggers import ErrorMessages

def check_minimum_elements(doc, messages=None):
    if isinstance(messages, list):
        raise TypeError("messages should be None or an instance of ErrorMessages")
    if messages is None:
        messages = ErrorMessages()

    messages.push_context(doc.name)
    check_components_names(doc, messages)
    check_components_versions(doc, messages)
    check_sbom_author(doc, messages)
    check_sbom_timestamp(doc, messages)
    check_sbom_dependency_relationships(doc, messages)
    check_components_suppliers(doc, messages)
    check_components_identifiers(doc, messages)
    messages.pop_context()
    return messages

def check_components_names(doc, messages):
    for package in doc.packages:
        messages = check_name(package, messages)

def check_components_versions(doc, messages):
    for package in doc.packages:
        messages = check_version(package, messages)

def check_sbom_author(doc, messages):
    if doc.creation_info.creators[1].name is None:
        messages.append("Document has no author.")

def check_sbom_timestamp(doc, messages):
    if doc.creation_info.created is None:
        messages.append("Document has no timestamp.")

def check_sbom_dependency_relationships(doc, messages):
    for relationship in doc.relationships:
        messages = check_relationship(relationship, messages)

def check_components_suppliers(doc, messages):
    for package in doc.packages:
        messages = check_supplier(package, messages)

def check_components_identifiers(doc, messages):
    for package in doc.packages:
        messages = check_identifier(package, messages)

def check_supplier(package, messages):
    # if package.supplier is None:
    #     messages.append("Package has no supplier.")
    return

def check_identifier(package, messages):
    if package.spdx_id is None:
        messages.append("Package has no identifier.")

def check_version(package, messages):
    if package.version is None:
        messages.append("Package has no version.")

def check_name(package, messages):
    if package.name is None:
        messages.append("Package has no name.")

def check_relationship(relationship, messages):
    if relationship is None:
        messages.append("Document has no relationship.")
