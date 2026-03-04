from clang.cindex import Index, CursorKind, TokenKind

def analyze_code(source_file):
    index = Index.create()
    
    # 1. PARSE THE CODE
    tu = index.parse(source_file)
    print(f"--- Analyzing: {source_file} ---\n")

    # ==========================================
    # TASK 1: IDENTIFY AND SEPARATE COMMENTS
    # ==========================================
    print("--- 1. COMMENT ANALYSIS ---")
    for token in tu.get_tokens(extent=tu.cursor.extent):
        if token.kind == TokenKind.COMMENT:
            comment_text = token.spelling
            if comment_text.startswith('//'):
                print(f"[Single-Line Comment]: {comment_text}")
            elif comment_text.startswith('/*'):
                print(f"[Multi-Line Comment]:  {comment_text}")
    
    print("\n")

    # ==========================================
    # TASK 2: SEGREGATE FUNCTIONS
    # ==========================================
    print("--- 2. FUNCTION NAMES ---")
    for node in tu.cursor.walk_preorder():
        if node.kind == CursorKind.FUNCTION_DECL:
            # Ensure we only print functions from our input file, not standard libraries
            if node.location.file and node.location.file.name == source_file:
                print(f"[Function Found]: {node.spelling}")

# Run the analyzer
if __name__ == "__main__":
    analyze_code("input.c")