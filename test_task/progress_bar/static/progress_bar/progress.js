$(document).ready(function() {
    const socket = new WebSocket('ws://' + window.location.host + '/ws/progress/');
    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const taskId = data.task_id;
        const progressElement = document.getElementById('progress-' + taskId);
        if (progressElement) {
            const progress = data.progress + '%';
            progressElement.style.width = progress;
            const resultMessage = document.getElementById('result-' + taskId);
            resultMessage.textContent = progress;
        }
    };

    $('#start-task-btn').click(function() {
        $.ajax({
            url: startTaskUrl,
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            success: function(response) {
                const taskId = response.task_id;
                $('#progress-container').append(`
                    <div id="task-${taskId}">
                        <h2>Task ${taskId}</h2>
                        <div id="progress-bar-${taskId}" style="width: 100%; background-color: #ddd; margin-top: 20px;">
                            <div id="progress-${taskId}" style="width: 0; height: 30px; background-color: #4caf50;"></div>
                        </div>
                        <h2 id="result-${taskId}"></h2>
                    </div>
                `);
            },
            error: function(xhr, status, error) {
                console.error('Error starting task:', error);
            }
        });
    });
});