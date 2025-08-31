import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout = "centered")

st.title("🎮 Tic Tac Toe")
st.write("        ")

st.markdown("""
            <style>
    button[kind="secondary"] {
        height:80px !important;
        width:80px !important;
        font-size:30px !important;
    }
    </style>
""", unsafe_allow_html=True)

if "board" not in st.session_state :
    st.session_state.board = [""]*9
if "winner" not in st.session_state :
    st.session_state.winner = None 
if "turn" not in st.session_state :
    st.session_state.turn = "X" 


def check_winner(board) :
    wins = [
        [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]             
    ]
    for a,b,c in wins:
        if (board[a] != " ") and board[a] == board[b] == board[c]:
            return board[a]   
    if "" not in board:
        return "Draw"
    return None


left, mid, right = st.columns([3,1,1])
with left :
    for row in range(3) :
        cols = st.columns(3, gap = "small")
        for col in range(3):
            i = row * 3 + col
            with cols[col] :
                if st.button(st.session_state.board[i] or "", key=i) :
                    if not st.session_state.board[i] and not st.session_state.winner :
                        st.session_state.board[i] = st.session_state.turn
                        st.session_state.winner = check_winner(st.session_state.board)
                    if not st.session_state.winner :   
                        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                    st.rerun()  

if st.session_state.winner :
    if st.session_state.winner == "Draw" :
        st.info("🤝 It's a Draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} Wins!")
else:
    st.write(f"👉 Player {st.session_state.turn}'s turn")


if st.button("Restart Game") :
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None