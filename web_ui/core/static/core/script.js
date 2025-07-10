// Game state variables
let selectedSquare = null;
let currentTurn = 'white';
let gameStatus = 'active';
let moveHistory = [];

// Initialize the chessboard
function initializeBoard() {
    const chessboard = $('#chessboard');
    chessboard.empty();

    const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const ranks = [8, 7, 6, 5, 4, 3, 2, 1];

    ranks.forEach((rank, rankIndex) => {
        files.forEach((file, fileIndex) => {
            const squareId = file + rank;
            const isLight = (rankIndex + fileIndex) % 2 === 0;

            const square = $('<div>')
                .attr('id', squareId)
                .addClass('square')
                .addClass(isLight ? 'light' : 'dark')
                .data('position', squareId);

            // Add coordinates
            if (fileIndex === 0) {
                $('<span>')
                    .addClass('coordinates rank-coordinate')
                    .text(rank)
                    .appendTo(square);
            }

            if (rankIndex === 7) {
                $('<span>')
                    .addClass('coordinates file-coordinate')
                    .text(file)
                    .appendTo(square);
            }

            chessboard.append(square);
        });
    });

    // Load initial board state from server
    loadBoardState();
}

// Load board state from server
function loadBoardState() {

}
